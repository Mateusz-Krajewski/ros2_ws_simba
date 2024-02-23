# ROS APP Documentation


## Services

| id | name | Desc |
| --- | --- | --- |
| 100 | tenso controller | |
| 101 | temp controller | |
| 103 | servo controller | |
| 104 | gpio controller | |


## srv
| name | desc | req | res |
| --- | --- | --- | --- |
| "/Engine/Tenso/Cal" | kalibracja tenso | ignorowane | Ok(True/False) |
| "/Engine/Servo/Set" | ustawienie pozycji servo mechanizmu | servo_id,position | Ok(True/False) |
| "/Engine/GPIO/Set" | ustawienie pinu GPIO | gpio_id , state | Ok(True/False) |

## msg
| name | desc | data |
| --- | --- | --- |
| "/Engine/HB" | status życia każdej aplikacji | app_id,timestamp |
| "/Engine/Tenso" | dane z tensobelki | tenso_id,waga |
| "/Engine/Temp" | dane z ds18b20 | temp_id, temperatura *C |
| "/Engine/Servo" | status servo | servo_id, servo_pos |



## Actuators

| id | name | string_id |
| --- | --- | --- |
| 100 | tenso controller | |
| 101 | temp controller | |
| 103 | servo controller | |
| 104 | gpio controller | |

## Sensors
100-199 - temperatura
200-299 - ciśnienie
300-399 - róż ciśnienia
400-499 - tenso
