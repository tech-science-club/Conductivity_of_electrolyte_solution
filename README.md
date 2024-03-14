Embedding programming into electrochemical investigations of electrolyte solutions 

we utilize the Python programming language along with its libraries and the Arduino board AtMega 2560. Python is used to design a framework that displays real-time data flow, while the AtMega2560 is employed to obtain analog signals, convert them into digital ones, send them to a PC, and process them as desired.

In physical chemistry, conductance is the reciprocal of the resistance of electrolyte solutions. Thus, by detecting the latter, we can:

- Measure conductance and use our equipment in conductometric titration to determine the equivalence point of a reaction, or in other words, obtain an analytical signal.
- Generate a titration curve in real-time mode.

For more detailed information, refer to [link1](https://en.wikipedia.org/wiki/Conductivity_(electrolytic))  and [link2](https://en.wikipedia.org/wiki/Conductometry).
	

The wiring circuit is as follows:

![Снимок экрана 2024-03-08 224809](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/32ab4ebf-6bf4-47b3-8753-52d14fb0c41c)

Additionally, I have added an LCD screen to improve the visualization of the process, a 1k Ohm resistor, and an electrolyte solution. I have used 2 graphite cores from a pencil as electrodes to minimize their participation in redox processes.

The Arduino board converts the analog signal into a digital one and transmits data to the PC via USB communication. A Python script retrieves the digital signal and processes it using the PySerial library. To filter out unnecessary data, such as characters, the 're' library has been utilized.

By employing the matplotlib library, we can visualize and analyze changes in our data. The maximum and minimum values are selected and can be observed in the bottom grid.


![Снимок экрана 2024-03-14 155026](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/9336580e-2784-4a45-877f-220d5b3aae48)

The Python script collects the retrieved data in a list and sends it to a remote web server, where it is posted onto a webpage and a corresponding plot is generated using PHP and chart.js scripts. 
Thus, we get this picture on our web page:

![Снимок экрана 2024-03-06 213225](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/40f8ed39-bf05-4c43-bb3e-c24a85408485)

Consequently, we obtain a visualization on our webpage that showcases the titration process of a solution of acetic acid (CH3COOH) with sodium hydroxide (NaOH). The endpoint of the neutralization reaction is indicated at 119 seconds with the lowest value of solution conductance, indicating that CH3COOH has fully reacted with the base, and any subsequent addition of it will increase conductance.    
It's important to note that all these measurements are for demonstrative purposes only and cannot be directly used for lab analyses. I have used reagents that are readily available from shops, and unfortunately, I do not have access to a chemical lab to calibrate measurements using standard solutions and lab equipment.


