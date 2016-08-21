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


package com.rabbitmq.client.test.server;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.test.functional.ClusteredTestBase;
import com.rabbitmq.tools.Host;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

/**
 * This tests whether 'absent' queues - durable queues whose home node
 * is down - are handled properly.
 */
public class AbsentQueue extends ClusteredTestBase {

    private static final String Q = "absent-queue";

    @Override protected void setUp() throws IOException, TimeoutException {
        super.setUp();
        if (clusteredConnection != null)
            stopSecondary();
    }

    @Override protected void tearDown() throws IOException, TimeoutException {
        if (clusteredConnection != null)
            startSecondary();
        super.tearDown();
    }

    @Override protected void createResources() throws IOException {
        alternateChannel.queueDeclare(Q, true, false, false, null);
    }

    @Override protected void releaseResources() throws IOException {
        alternateChannel.queueDelete(Q);
    }

    public void testNotFound() throws IOException {
        assertNotFound(new Task() {
                public void run() throws IOException {
                    channel.queueDeclare(Q, true, false, false, null);
                }
            });
        assertNotFound(new Task() {
                public void run() throws IOException {
                    channel.queueDeclarePassive(Q);
                }
            });
        assertNotFound(new Task() {
                public void run() throws IOException {
                    channel.queuePurge(Q);
                }
            });
        assertNotFound(new Task() {
                public void run() throws IOException {
                    channel.basicGet(Q, true);
                }
            });
        assertNotFound(new Task() {
                public void run() throws IOException {
                    channel.queueBind(Q, "amq.fanout", "", null);
                }
            });
    }

    protected void assertNotFound(Task t) throws IOException {
        if (clusteredChannel == null) return;
        try {
            t.run();
            if (!HATests.HA_TESTS_RUNNING) fail("expected not_found");
        } catch (IOException ioe) {
            assertFalse(HATests.HA_TESTS_RUNNING);
            checkShutdownSignal(AMQP.NOT_FOUND, ioe);
            channel = connection.createChannel();
        }

    }

    private interface Task {
        public void run() throws IOException;
    }

}
