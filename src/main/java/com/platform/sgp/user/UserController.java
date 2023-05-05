package com.platform.sgp.user;

import com.platform.sgp.user.model.UserRequestDTO;
import com.platform.sgp.user.model.UserResponseDTO;
import com.platform.sgp.user.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/user")
public class UserController {

    @Autowired
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/info")
    public ResponseEntity<UserResponseDTO> getUserInformation(@RequestBody UserRequestDTO userRequestDTO) {
        UserResponseDTO userResponseDTO = userService.getUserInformation(userRequestDTO.getUsername(), userRequestDTO.getEmail());
        return ResponseEntity.ok(userResponseDTO);
    }
}
