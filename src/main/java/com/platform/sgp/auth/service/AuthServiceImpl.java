package com.platform.sgp.auth.service;

import org.springframework.stereotype.Service;

@Service
public class AuthServiceImpl implements AuthService {

    @Override
    public String logInByEmailPassword(String email, String password) {
        return "name.surname@sgp.com".equals(email) && "name1234".equals(password) ? "log-in" : "";
    }

    @Override
    public String signUpWithUsernameEmailPassword(String username, String email, String password) {
        return "sign-up";
    }
}
