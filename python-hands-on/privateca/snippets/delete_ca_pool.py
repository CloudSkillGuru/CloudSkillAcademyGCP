#!/usr/bin/env python

# Copyright 2021 Google LLC
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

# [START privateca_delete_ca_pool]
import google.cloud.security.privateca_v1 as privateca_v1


def delete_ca_pool(project_id: str, location: str, ca_pool_name: str) -> None:
    """
    Delete the CA pool as mentioned by the ca_pool_name.
    Before deleting the pool, all CAs in the pool MUST BE deleted.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
        ca_pool_name: the name of the CA pool to be deleted.
    """

    caServiceClient = privateca_v1.CertificateAuthorityServiceClient()

    ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)

    # Create the Delete request.
    request = privateca_v1.DeleteCaPoolRequest(name=ca_pool_path)

    # Delete the CA Pool.
    caServiceClient.delete_ca_pool(request=request)

    print("Deleted CA Pool:", ca_pool_name)


# [END privateca_delete_ca_pool]
