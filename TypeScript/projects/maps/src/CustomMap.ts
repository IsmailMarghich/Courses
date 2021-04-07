/*instead of just using the default map from the google api, we will make our own to prevent others from breaking it
 * all u can do with this custom map is adding markers and none of the google map methods*/
/*an interface that we can use to allow people to easily add markers to our map as long as they have a location object with a lat and long and a content method*/
interface Mappable {
  location: {
    lat: number;
    lng: number;
  };
  /*a function returns the content to be displayed when the marker is pressd*/
  markerContent(): string;
}
export class CustomMap {
  private googleMap: google.maps.Map; /*make our map private, so only this class can access it, and no code outside of the class can break it*/
  /*were gonna pass an id argument so we can tell the class where to place the map*/
  constructor(divId: string) {
    /*create our own instance of a google map*/
    this.googleMap = new google.maps.Map(document.getElementById(divId), {
      zoom: 1,
      center: {
        lat: 0,
        lng: 0,
      },
    });
  }
  /*this function takes anything that matches our interface, this allows us to add more markers of different classes in the future easily*/
  addMarker(place: Mappable) {
    const marker = new google.maps.Marker({
      map: this.googleMap,
      position: {
        lat: place.location.lat,
        lng: place.location.lng,
      },
    }); /*when a user presses a marker we want to show an info box with information about the location*/
    marker.addListener("click", () => {
      const infoWindow = new google.maps.InfoWindow({
        content: place.markerContent(),
      });
      infoWindow.open(this.googleMap, marker);
    });
  }
}
