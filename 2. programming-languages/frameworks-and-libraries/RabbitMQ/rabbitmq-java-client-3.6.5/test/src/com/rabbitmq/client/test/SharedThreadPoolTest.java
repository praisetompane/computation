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

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.impl.AMQConnection;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeoutException;

public class SharedThreadPoolTest extends BrokerTestCase {
    public void testWillShutDownExecutor() throws IOException, TimeoutException {
        ConnectionFactory cf = new ConnectionFactory();
        ExecutorService executor = Executors.newFixedThreadPool(8);
        cf.setSharedExecutor(executor);

        AMQConnection conn1 = (AMQConnection)cf.newConnection();
        assertFalse(conn1.willShutDownConsumerExecutor());

        AMQConnection conn2 = (AMQConnection)cf.newConnection(Executors.newSingleThreadExecutor());
        assertFalse(conn2.willShutDownConsumerExecutor());

        AMQConnection conn3 = (AMQConnection)cf.newConnection((ExecutorService)null);
        assertTrue(conn3.willShutDownConsumerExecutor());

        cf.setSharedExecutor(null);

        AMQConnection conn4 = (AMQConnection)cf.newConnection();
        assertTrue(conn4.willShutDownConsumerExecutor());
    }
}
