# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http:# www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

DJANGO_APPS = [ "kafka" ]
REQUIRES_HADOOP = False
MENU_INDEX = 100
NICE_NAME = "Kafka"
ICON = "kafka/art/icon_kafka_24.png"
IS_URL_NAMESPACED = True

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
METRICS_INI = os.path.join(PROJECT_ROOT, 'metrics.ini')
