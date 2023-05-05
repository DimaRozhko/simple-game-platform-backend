package com.platform.sgp.gameprocess.service;

import com.platform.sgp.user.model.UserResponseDTO;
import org.springframework.stereotype.Service;

@Service
public class GameProcessImpl implements GameProcess {


    @Override
    public String setStartTime(String startTime, String email) {
        return startTime;
    }

    @Override
    public String setEndTime(String endTime, String email) {
        return endTime;
    }

    @Override
    public String getGameTime(String startTime, String endTime, String email) {
        return "00:14:17";
    }
}
