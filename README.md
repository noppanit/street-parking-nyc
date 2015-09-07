# Street Parking Signs NYC
A server for all street parking signs in NYC

# Create Table

Connect to Heroku by running this command in your project

```
heroku pg:psql --app street-parking DATABASE
```

And paste the script below.

```
CREATE TABLE SIGNS (
	longtitude float,
	latitude float,
	OBJECTID integer,
	SG_KEY_BOR varchar(10),
	SG_ORDER_N varchar(10),
	SG_SEQNO_N varchar(3),
	SG_MUTCD_C varchar(10),
	SR_DIST integer,
	SG_SIGN_FC varchar(5),
	SG_ARROW_D varchar(5),
	x float,
	y float,
	SIGNDESC1 varchar(300)
);
```

# Import

```
heroku pg:psql --app street-parking DATABASE -c "\copy signs FROM 'Signs.csv' WITH CSV HEADER DELIMITER AS ',';"
```

# Enable functions

You have to enable extensions in Postgresql in order to use special functions. 

```
CREATE EXTENSION cube;
```

```
CREATE EXTENSION earthdistance;
```

# Create Index for Latitude and Longtitude

```
CREATE INDEX signs_lat_long on signs USING gist(ll_to_earth(latitude, longtitude));
```

This will pre-calculate the degrees for each of the coordinates that will make the above queries run much faster as it's not doing those calculations on each row for each run.

# To Test

Don't for get to use the latitude and longtitude from NYC as the data is only in NYC

```
SELECT * from signs WHERE earth_box(ll_to_earth(40.7135097, -73.9859414), 1000) @> ll_to_earth(latitude, longtitude);
```

# API Test

After you've run the application by

```
python server.py
```

Then try this URL

```
http://localhost:5000/find?lat=40.7135097&lng=-73.9859414&radius=1000
```

# References

[http://johanndutoit.net/searching-in-a-radius-using-postgres/](http://johanndutoit.net/searching-in-a-radius-using-postgres/)

