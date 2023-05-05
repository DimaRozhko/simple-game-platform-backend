package com.platform.sgp.user.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class UserResponseDTO {
    private String email;
    private String username;
    private String favoriteGame;
    private String bestTime;
}
