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

import java.io.IOException;

import com.rabbitmq.client.impl.AMQConnection;
import com.rabbitmq.client.test.BrokerTestCase;

public class Heartbeat extends BrokerTestCase {

    public Heartbeat()
    {
        super();
        connectionFactory.setRequestedHeartbeat(1);
    }

    public void testHeartbeat()
        throws IOException, InterruptedException
    {
        assertEquals(1, connection.getHeartbeat());
        Thread.sleep(3100);
        assertTrue(connection.isOpen());
        ((AMQConnection)connection).setHeartbeat(0);
        assertEquals(0, connection.getHeartbeat());
        Thread.sleep(3100);
        assertFalse(connection.isOpen());

    }

}
