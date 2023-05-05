package com.platform.sgp.gameprocess.service;

public interface GameProcess {

    public String setStartTime(String startTime, String email);
    public String setEndTime(String endTime, String email);

    public String getGameTime(String startTime, String endTime, String email);
}
