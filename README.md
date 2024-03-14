Embedding programing into electrochemical investigation of electrolytes solution. 

We have Python program language with its libraries and Arduino board AtMega 2560. The first one is being used to design frame, which going to show us real-time data flow. The AtMega2560 is being used to get analogue signal and convert it into digital one, send to PC and treat it in desired way.
As far as we know from physical chemistry, conductance is reciprocical of the resistance of electrolyte solutions. Hence detecting last one we can: 
-	measure conductance and use our equipment in conductometrical titration to get equivalent point of reaction, in other words, we can get analytical signal.
-	build titration curve in real time mode.
	
Detail information you can get over here https://en.wikipedia.org/wiki/Conductivity_(electrolytic)
and here https://en.wikipedia.org/wiki/Conductometry.

The wire circuit is following:

![Снимок экрана 2024-03-08 224809](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/32ab4ebf-6bf4-47b3-8753-52d14fb0c41c)

Here have been added lcd screen to get better view on process, 1k Ohm resistor and a electrolyte solution. Have been used 2 graphite cores from pencil as electrodes to minimize it’s participation in Red – Ox processes. 

The Arduino board converts analogue signal into digital one, passes data to the pc via usb com communication. Python script gets digital signal and treat it with the help of PySerial library. To sort out unnecessary data, such as characters etc re library has been used.
Using matplotlib library we can build and visualise our data and analyse it’s changes. The max and min values are selecting and can be notable in the bottom grid.


![Снимок экрана 2024-03-14 155026](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/9336580e-2784-4a45-877f-220d5b3aae48)

Python script collects retrieved data in list and send it to the remote web server, post data into webpage and build correspondent plot with the help of php and chart.js scripts. 
Consequently, we get this picture on our web page:

![Снимок экрана 2024-03-06 213225](https://github.com/tech-science-club/Conductivity-of-solution/assets/130900888/40f8ed39-bf05-4c43-bb3e-c24a85408485)

In brief, here is a process of the titration of solution of acetate acid CH3COOH with base NaOH. It points at the end-point of neutralisation reaction which is visible at 119 sec with the lowest value of solution conductance at that moment, that means CH3COOH had fully reacted with base and very next portion of it will increase conductance.    
All these measurements are just with demonstrative purpose and can’t be used in lab analyses directly from here. 
Here have been used reactives, which is possible to get from shop, and unfortunately I have not access to a chemical lab to calibrate measurements with the help of standard solution and lab equipment. 


