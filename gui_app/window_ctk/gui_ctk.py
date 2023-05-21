#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

"""
Project Name: 'crypto-wallet-list'
Version: 0.1

Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""


import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class GUI_ctk(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.app_ctk = self
        self.app_ctk.geometry("400x240")
        self.app_ctk.title("Crypto Wallet List")
