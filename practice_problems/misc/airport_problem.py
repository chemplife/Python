'''
We are an Airlines and we have Flights that goes to a list of Airports (airports).
And we have list of one-way routes from one airport to another (routes)

airports= ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
routes = [["DSM", "ORD"], ["ORD", "BGI"], ["BGI", "LGA"], ["SIN", "CDG"], ["CDG", "SIN"], ["CDG", "BUD"], ["DEL", "DOH"], ["DEL", "CDG"],\
			["TLV", "DEL"], ["EWR", "HND"], ["HND", "ICN"], ["HND", "JFK"], ["ICN", "JFK"], ["JFK", "LGA"], ["EYW", "LHR"], ["LHR", "SFO"],\
			["SFO", "SAN"], ["SFO", "DSM"], ["SAN", "EYW"]]

we want our customers to be able to travel from any airport, to any airport.

So, if a passenger starts from airport (startingAirport), they should be able to travel to any airport they want
startingAirport = "LGA"

Find a minimized number of one-way flights (routes) a passenger needs / allowed to take to be able to reach any airport they want..

(Actual Solution time: 45 minutes)

My Approach:
There are NO outbound flights from 'LGA'
So, our function need to take care of 2 cases:
1. startingPoint HAS outbound flights
2. startingPoint Does Not have any outbound flight

To find route to the airport with most outbound flights.

1.
For Has outbound flights
If airport is 0th element of each pair.

Depending on the number of outbound flights, we can rank the airports
If the destination_airport is not the direct connected one (minimum connections cannot be 1 now), go to the airport with least rank
search through until we get dest_connection= 2, if not 2 then 3.. and so on..

How to search through?
1. Check the connection of the airport.
2. for each of those connections: select the least ranked airport and check the connections
3. iterate over all the connections and we will find a route to the dest_airport

If the dest_connection = 2, we are good
Anythign more than 2,
1. Iterate backwards from the dest_airport and see which airport is direct connection from 'startingAirport' or 
'''