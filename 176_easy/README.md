#### Description

An interesting way to represent data is a pivot table. If you use spreadsheet programs like Excel you might have seen these before. If not then you are about to enjoy it.

Say you have data that is related in three parts. We can field this in a table with column and rows and the middle intersection is a related field. For this challenge you will need to make a pivot table for a wind energy farm. These farms of wind mills run several windmills with tower numbers. They generate energy measured in kilowatt hours (kWh).

You will need to read in raw data from the field computers that collect readings throughout the week. The data is not sorted very well. You will need to display it all in a nice pivot table.

Top Columns should be the days of the week.
Side Rows should be the tower numbers and the data in the middle the total kWh hours produced for that tower on that day of the week.

#### Input

The challenge input is 1000 lines of the computer logs. You will find it [HERE - gist of it](https://gist.github.com/coderd00d/ca718df8e633285885fa)

The log data is in the format:

    (tower #) (day of the week) (kWh)

#### Output

A nicely formatted pivot table to report to management of the weekly kilowatt hours of the wind farm by day of the week.

#### My Output

    Tower   Sun     Mon     Tue     Wed     Thu     Fri     Sat
    1009	895     237     967     556  	687  	842  	749
    1008	728     709  	374  	485  	560  	836  	864
    1007	536     947  	976  	733  	640  	941  	876
    1006	639     638  	568  	826  	754	    1118	857
    1005	812     637  	1129	695 	648  	449  	445
    1004	874  	696  	783  	546  	646  	1184	813
    1003	390  	607  	372  	399  	583  	624  	383
    1002	586  	510  	733  	862  	793  	1013	530
    1001	749  	279  	662  	907  	561  	752  	501
    1000	740  	624  	385  	677  	443  	810  	1005
