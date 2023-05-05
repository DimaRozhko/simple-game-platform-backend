package com.platform.sgp.auth.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class SignUpDTO {
    private String username;
    private String email;
    private String password;
}
