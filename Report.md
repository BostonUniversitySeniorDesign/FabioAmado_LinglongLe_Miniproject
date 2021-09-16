# EC463 Hardware Mini Project Report
**Fabio Amado, Linglong Le** 

This is the Report for the Hardware Miniproject Assigned to Electrical Engineers for EC463, Fall 2021.
## Wifi Section
#### Extended Wifi Data Plot
![15 Minute Wifi Plot](./wifi_data_results/wifi_2021-09-14T12_43_54_results.png)

#### Discussion and Explanation of the Plot
The link above contains the plotted result from an extended wifi scan, which ran for around 35 minutes, from 12:45 PM to 1:20 PM. In this plot, it is clear that there was some variation in the amount of cars detected at any one time, with the amount of cars detected ranging from 0 to 11 at any given time. In the plot there were periods of relatively high activity from 12:47 PM to 12:53 PM and from 1:03 PM to 1:13 PM, while the almost no activity was detected from 12:53 PM to 1:02 PM. Analyzing the results, it is clear that there were more cars passing by during the periods of high activity, while there was a lull in traffic during the period of low activity. 

One reason for this pattern could be due to workers returning from their lunch break. The period of highest activity was in the region of 12:47 PM to 12:53 PM, which is just before most peoples lunch breaks end. Thus the increased traffic in this period could be from people hoping to be back into their workplaces before 1:00pm after having lunch. The peaks in activity from 1:03 to 1:13 PM could also be attributed to lunch breaks. Workplaces could have been holding company activities or group lunches that were scheduled from 12:00 PM to 1:00 pm, and as such would not be worried about being back in the office before 1:00 pm. At no point in time of this scan however, were there any deadlocks or periods of extreme congestion, as shown by the variance in the data minute by minute. Had a traffic jam occurred, then there would be a more consistent amount of cars over time, without the jumps between highs and lows in the amount of detected cars.

## Bluetooth Section

#### Extended Wifi Data Plot
![Bluetooth Data Plot](./bluetooth_data_results/Bluetooth_Device_Plot.png)
### Bluetooth Data
1st scan: 24, Buds Pro, Bose AE2 SoundLink  
2nd scan: 64, Buds, LE, Bose, Tile  
3rd scan: 35, Buds, Tile, Bose  
4th scan: 32, Buds Bose, Tile, Galaxy  
5th scan: 42, Buds, Bose, Galaxy, Tile  
6th scan: 25, Buds, Galaxy, Tile, LE, Bose  
7th scan: 24, Buds, Galaxy, Tile, LE, Bose  
8th scan: 27, Buds, Galaxy, Tile, LE, Bose  
9th scan: 26, Buds, Galaxy, Tile, Bose  
10th scan: 28, Buds, Galaxy, Tile, Bose

#### Discussion and Explanation of Data
The data above contains the bluetooth scan results from 9 thirty seconds scans and one 5 minute scan. The rasberry pi read the bluetooth devices in its proximity and compiled the data showing the u as the IP address and the n as the device name. Looking at data it can be seen that the pedestrian foottraffic wasn't as much as the wifi scan since the number of data received was less significant than the data results. As the results show using the wifi scan would be a better option than the bluetooth scan as you can read more devices such as modern automobiles and fixed beacons such as TVs, speakers, and modern automobiles.

## Difficulties Experienced:
The main difficulties experienced were in the initial setup and startup of the Raspberry Pi. For the Raspberry Pi to properly display to the HDM monitor, it had to have the connections to the HDMI port, mousepad, and keyboard before power was supplied. Additionally, the Raspberry Pi had troubles with connecting to the BU campus Wifi. To solve this, a mobile hotspot was used instead to connect to the internet so that the scans could proceed.
