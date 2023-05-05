package com.platform.sgp.user.service;

import com.platform.sgp.user.model.UserResponseDTO;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Override
    public UserResponseDTO getUserInformation(String username, String email) {
        return new UserResponseDTO(email, username, "15", "00:14:17");
    }
}
