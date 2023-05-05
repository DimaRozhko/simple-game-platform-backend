package com.platform.sgp.auth;

import com.platform.sgp.auth.model.SignUpDTO;
import com.platform.sgp.auth.service.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(path = "/auth")
public class AuthController {

    @Autowired
    private final AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }

    @GetMapping("/log-in")
    public ResponseEntity<String> logIn(@RequestParam(value = "email") String email,
                                        @RequestParam(value = "password") String password) {
        String refreshToken = authService.logInByEmailPassword(email, password);
        return refreshToken.isEmpty() ?
                ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("") :
                ResponseEntity.ok(refreshToken);
    }

    @PostMapping("/sign-up")
    public ResponseEntity<String> signUp(@RequestBody SignUpDTO signUpDTO) {
        String refreshToken = authService.signUpWithUsernameEmailPassword(signUpDTO.getUsername(), signUpDTO.getEmail(), signUpDTO.getPassword());
        return refreshToken.isEmpty() ?
                ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("") :
                ResponseEntity.ok(refreshToken);
    }
}
