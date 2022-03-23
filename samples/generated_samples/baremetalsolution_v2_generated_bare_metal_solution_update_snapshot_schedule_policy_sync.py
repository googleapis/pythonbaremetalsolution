# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateSnapshotSchedulePolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-bare-metal-solution


# [START baremetalsolution_v2_generated_BareMetalSolution_UpdateSnapshotSchedulePolicy_sync]
from google.cloud import bare_metal_solution_v2


def sample_update_snapshot_schedule_policy():
    # Create a client
    client = bare_metal_solution_v2.BareMetalSolutionClient()

    # Initialize request argument(s)
    request = bare_metal_solution_v2.UpdateSnapshotSchedulePolicyRequest(
    )

    # Make the request
    response = client.update_snapshot_schedule_policy(request=request)

    # Handle the response
    print(response)

# [END baremetalsolution_v2_generated_BareMetalSolution_UpdateSnapshotSchedulePolicy_sync]
