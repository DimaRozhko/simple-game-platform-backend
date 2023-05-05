package com.platform.sgp.user.service;

import com.platform.sgp.user.model.UserResponseDTO;

public interface UserService {

    public UserResponseDTO getUserInformation(String username, String email);
}
