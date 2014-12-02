package waypoint

import "fmt"

type Point struct {
	Latitude  float32
	Longitude float32
}

func New(lat, long float32) *Point {
	return &Point{lat, long}
}

func (p *Point) String() string {
	return fmt.Sprintf("Point{%f, %f}", p.Latitude, p.Longitude)
}
