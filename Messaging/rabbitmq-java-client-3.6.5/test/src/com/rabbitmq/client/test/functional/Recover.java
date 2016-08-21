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


package com.rabbitmq.client.test.functional;

import java.util.Arrays;
import java.io.IOException;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.QueueingConsumer;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Command;
import com.rabbitmq.client.ShutdownSignalException;

import com.rabbitmq.client.test.BrokerTestCase;

public class Recover extends BrokerTestCase {

    String queue;
    final byte[] body = "message".getBytes();

    public void createResources() throws IOException {
        AMQP.Queue.DeclareOk ok = channel.queueDeclare();
        queue = ok.getQueue();
    }

    static interface RecoverCallback {
        void recover(Channel channel) throws IOException;
    }

    // The AMQP specification under-specifies the behaviour when
    // requeue=false.  So we can't really test any scenarios for
    // requeue=false.

    void verifyRedeliverOnRecover(RecoverCallback call)
        throws IOException, InterruptedException {
        QueueingConsumer consumer = new QueueingConsumer(channel);
        channel.basicConsume(queue, false, consumer); // require acks.
        channel.basicPublish("", queue, new AMQP.BasicProperties.Builder().build(), body);
        QueueingConsumer.Delivery delivery = consumer.nextDelivery();
        assertTrue("consumed message body not as sent",
                   Arrays.equals(body, delivery.getBody()));
        // Don't ack it, and get it redelivered to the same consumer
        call.recover(channel);
        QueueingConsumer.Delivery secondDelivery = consumer.nextDelivery(5000);
        assertNotNull("timed out waiting for redelivered message", secondDelivery);
        assertTrue("consumed (redelivered) message body not as sent",
                   Arrays.equals(body, delivery.getBody()));
    }

    void verifyNoRedeliveryWithAutoAck(RecoverCallback call)
        throws IOException, InterruptedException {
        QueueingConsumer consumer = new QueueingConsumer(channel);
        channel.basicConsume(queue, true, consumer); // auto ack.
        channel.basicPublish("", queue, new AMQP.BasicProperties.Builder().build(), body);
        QueueingConsumer.Delivery delivery = consumer.nextDelivery();
        assertTrue("consumed message body not as sent",
                   Arrays.equals(body, delivery.getBody()));
        call.recover(channel);
        assertNull("should be no message available", channel.basicGet(queue, true));
    }

    final RecoverCallback recoverSync = new RecoverCallback() {
            public void recover(Channel channel) throws IOException {
                channel.basicRecover(true);
            }
        };

    final RecoverCallback recoverSyncConvenience = new RecoverCallback() {
            public void recover(Channel channel) throws IOException {
                channel.basicRecover();
            }
        };

    public void testRedeliveryOnRecover() throws IOException, InterruptedException {
        verifyRedeliverOnRecover(recoverSync);
    }
    
    public void testRedeliverOnRecoverConvenience() 
        throws IOException, InterruptedException {
        verifyRedeliverOnRecover(recoverSyncConvenience);
    }

    public void testNoRedeliveryWithAutoAck()
        throws IOException, InterruptedException {
        verifyNoRedeliveryWithAutoAck(recoverSync);
    }

    public void testRequeueFalseNotSupported() throws Exception {
        try {
            channel.basicRecover(false);
            fail("basicRecover(false) should not be supported");
        } catch(IOException ioe) {
            checkShutdownSignal(AMQP.NOT_IMPLEMENTED, ioe);
        }
    }
}
