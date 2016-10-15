// Copyright (c) 2007-Present Pivotal Software, Inc.  All rights reserved.
//
// This software, the RabbitMQ Java client library, is triple-licensed under the
// Mozilla Public License 1.1 ("MPL"), the GNU General Public License version 2
// ("GPL") and the Apache License version 2 ("ASL"). For the MPL, please see
// LICENSE-MPL-RabbitMQ. For the GPL, please see LICENSE-GPL2.  For the ASL,
// please see LICENSE-APACHE2.
//
// This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND,
// either express or implied. See the LICENSE file for specific language governing
// rights and limitations of this software.
//
// If you have any questions regarding licensing, please contact us at
// info@rabbitmq.com.

package com.rabbitmq.client.test;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.QueueingConsumer;
import com.rabbitmq.client.ShutdownSignalException;

public class QueueingConsumerShutdownTests extends BrokerTestCase{
  static final String QUEUE = "some-queue";
  static final int THREADS = 5;

  public void testNThreadShutdown() throws Exception{
    Channel channel = connection.createChannel();
    final QueueingConsumer c = new QueueingConsumer(channel);
    channel.queueDeclare(QUEUE, false, true, true, null);
    channel.basicConsume(QUEUE, c);
    final AtomicInteger count = new AtomicInteger(THREADS);
    final CountDownLatch latch = new CountDownLatch(THREADS);

    for(int i = 0; i < THREADS; i++){
      new Thread(){
        @Override public void run(){
          try {
            while(true){
                c.nextDelivery();
            }
          } catch (ShutdownSignalException sig) {
              count.decrementAndGet();
          } catch (Exception e) {
            throw new RuntimeException(e);
          } finally {
            latch.countDown();
          }
        }
      }.start();
    }

    connection.close();

    // Far longer than this could reasonably take
    assertTrue(latch.await(5, TimeUnit.SECONDS));
    assertEquals(0, count.get());
  }

}
