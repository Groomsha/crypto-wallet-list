"""
Project Name: 'crypto-wallet-list'
Description: Crypto Wallet List

Ihor Cheberiak (c) 2023
https://www.linkedin.com/in/ihor-cheberiak/
"""

import customtkinter


class SettingsFrame:
    def __init__(self, ctk: customtkinter.CTkFrame) -> None:
        self.window = ctk

        # self.navigation_frame_label = customtkinter.CTkLabel(self.window, text="Navigation", image=None,
        #                                                      compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_frame = customtkinter.CTkFrame(self.window, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.window, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=1, column=0, padx=20, pady=10, sticky="s")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
