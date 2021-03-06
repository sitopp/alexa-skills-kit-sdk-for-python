# -*- coding: utf-8 -*-
#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
#
import unittest

from ask_sdk_model import RequestEnvelope, Context, User, Device
from ask_sdk_model.interfaces.system import SystemState
from ask_sdk_core.exceptions import PersistenceException
from ask_sdk_dynamodb.partition_keygen import (
    user_id_partition_keygen, device_id_partition_keygen)


class TestPartitionKeyGenerators(unittest.TestCase):
    def setUp(self):
        self.request_envelope = RequestEnvelope()
        self.context = Context()
        self.system = SystemState()
        self.user = User()
        self.device = Device()

    def test_valid_user_id_partition_keygen(self):
        self.user.user_id = "123"
        self.system.user = self.user
        self.context.system = self.system
        self.request_envelope.context = self.context

        assert user_id_partition_keygen(self.request_envelope) == "123", (
            "User Id Partition Key Generation retrieved wrong user id from "
            "valid request envelope")

    def test_user_id_partition_keygen_raise_error_when_request_envelope_null(self):
        with self.assertRaises(PersistenceException) as exc:
            user_id_partition_keygen(request_envelope=None)

        assert "Couldn't retrieve user id from request envelope" in str(
            exc.exception), (
            "User Id Partition Key Generation didn't throw exception when "
            "null request envelope is provided")

    def test_user_id_partition_keygen_raise_error_when_context_null(self):
        with self.assertRaises(PersistenceException) as exc:
            user_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve user id from request envelope" in str(
            exc.exception), (
            "User Id Partition Key Generation didn't throw exception when "
            "null context provided in request envelope")

    def test_user_id_partition_keygen_raise_error_when_system_null(self):
        self.request_envelope.context = self.context

        with self.assertRaises(PersistenceException) as exc:
            user_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve user id from request envelope" in str(
            exc.exception), (
            "User Id Partition Key Generation didn't throw exception when "
            "null system provided in context of "
            "request envelope")

    def test_user_id_partition_keygen_raise_error_when_user_null(self):
        self.context.system = self.system
        self.request_envelope.context = self.context

        with self.assertRaises(PersistenceException) as exc:
            user_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve user id from request envelope" in str(
            exc.exception), (
            "User Id Partition Key Generation didn't throw exception when "
            "null user provided in context.system of "
            "request envelope")

    def test_valid_device_id_partition_keygen(self):
        self.device.device_id = "123"
        self.system.device = self.device
        self.context.system = self.system
        self.request_envelope.context = self.context

        assert device_id_partition_keygen(self.request_envelope) == "123", (
            "Device Id Partition Key Generation retrieved wrong device id "
            "from valid request envelope")

    def test_device_id_partition_keygen_raise_error_when_request_envelope_null(self):
        with self.assertRaises(PersistenceException) as exc:
            device_id_partition_keygen(request_envelope=None)

        assert "Couldn't retrieve device id from request envelope" in str(
            exc.exception), (
            "Device Id Partition Key Generation didn't throw exception when "
            "null request envelope is provided")

    def test_device_id_partition_keygen_raise_error_when_context_null(self):
        with self.assertRaises(PersistenceException) as exc:
            device_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve device id from request envelope" in str(
            exc.exception), (
            "Device Id Partition Key Generation didn't throw exception when "
            "null context provided in request envelope")

    def test_device_id_partition_keygen_raise_error_when_system_null(self):
        self.request_envelope.context = self.context

        with self.assertRaises(PersistenceException) as exc:
            device_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve device id from request envelope" in str(
            exc.exception), (
            "Device Id Partition Key Generation didn't throw exception when "
            "null system provided in context of "
            "request envelope")

    def test_device_id_partition_keygen_raise_error_when_device_null(self):
        self.context.system = self.system
        self.request_envelope.context = self.context

        with self.assertRaises(PersistenceException) as exc:
            device_id_partition_keygen(request_envelope=self.request_envelope)

        assert "Couldn't retrieve device id from request envelope" in str(
            exc.exception), (
            "Device Id Partition Key Generation didn't throw exception when "
            "null device provided in context.system of "
            "request envelope")

    def tearDown(self):
        self.request_envelope = None
        self.context = None
        self.system = None
        self.user = None
        self.device = None
