package com.platform.sgp.auth.service;

public interface AuthService {

    public String logInByEmailPassword(String email, String password);
    public String signUpWithUsernameEmailPassword(String username, String email, String password);
}
