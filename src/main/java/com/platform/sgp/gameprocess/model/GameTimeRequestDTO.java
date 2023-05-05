package com.platform.sgp.gameprocess.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class GameTimeRequestDTO {
    private String email;
    private String startTime;
    private String endTime;
}
