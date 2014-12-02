package main

import (
	//"database/sql"
	"encoding/json"
	"fmt"
	"github.com/zenazn/goji"
	"github.com/zenazn/goji/web"
	"navserv/waypoint"
	"net/http"
)

type Route struct {
	Name      string
	Waypoints []*waypoint.Point
}

func (r *Route) Add(p *waypoint.Point) {
	r.Waypoints = append(r.Waypoints, p)
}

//var db *sql.DB

func main() {
	// connect to database
	//db, err = sql.Open(driverName, dataSourceName)

	goji.Get("/routes/:item", routeGet)
	goji.Post("/routes/:item", routePost)
	goji.Serve()
}

func routeGet(c web.C, rw http.ResponseWriter, req *http.Request) {
	// retrieve a route from database.

	// Always return the same route for testing.
	route := new(Route)
	route.Name = c.URLParams["item"]
	route.Add(waypoint.New(0.0, 0.0))
	route.Add(waypoint.New(1.1, 1.1))

	out, err := json.Marshal(route)
	if err != nil {
		// shouldn't happen in this testcase.
	}

	fmt.Fprintf(rw, "%s", out)
}

func routePost(c web.C, rw http.ResponseWriter, req *http.Request) {
	// update existing route
	err := req.ParseForm()
	if err != nil {
		fmt.Println("POST:", err)
	}

}
