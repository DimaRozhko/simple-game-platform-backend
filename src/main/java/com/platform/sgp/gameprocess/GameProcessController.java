package com.platform.sgp.gameprocess;

import com.platform.sgp.gameprocess.model.GameTimeRequestDTO;
import com.platform.sgp.gameprocess.service.GameProcess;
import com.platform.sgp.user.model.UserRequestDTO;
import com.platform.sgp.user.model.UserResponseDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(path = "/game-process")
public class GameProcessController {
    @Autowired
    private final GameProcess gameProcess;

    public GameProcessController(GameProcess gameProcess) {
        this.gameProcess = gameProcess;
    }

    @PostMapping("/start-time")
    public ResponseEntity<String> getStartTime(@RequestParam(value = "startTime") String startTime,
                                               @RequestParam(value = "email") String email) {
        return ResponseEntity.ok(gameProcess.setStartTime(startTime, email));
    }

    @PostMapping("/end-time")
    public ResponseEntity<String> getEndTime(@RequestParam(value = "endTime") String endTime,
                                             @RequestParam(value = "email") String email) {
        return ResponseEntity.ok(gameProcess.setEndTime(endTime, email));
    }

    @GetMapping("/game-time")
    public ResponseEntity<String> getGameTime(@RequestBody GameTimeRequestDTO gameTimeRequestDTO) {
        return ResponseEntity.ok(gameProcess.getGameTime(gameTimeRequestDTO.getStartTime(),
                gameTimeRequestDTO.getEndTime(), gameTimeRequestDTO.getEmail()));
    }
}
