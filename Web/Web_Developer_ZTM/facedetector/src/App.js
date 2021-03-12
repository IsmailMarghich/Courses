import './App.css';
import React, { Component} from 'react';
import Navigation from "./components/Navigation/Navigation";
import Logo from "./components/Logo/Logo";
import ImageLinkForm from "./components/ImageLinkForm/ImageLinkForm";
import Rank from "./components/Rank/Rank";
import Particles from "react-particles-js";
const particleOptions = {"particles": {
    "number": {
        "value": 50
    },
    "size": {
        "value": 4
    }
}, /*our options for our particles background*/
"interactivity": {
    "events": {
        "onhover": {
            "enable": true,
            "mode": "grab"
        }
    }
}
}
class App extends Component{
    render() {
        return (
        <div className="App">
            <Particles className='particles'
                params={particleOptions} />
            <h1>Face Detector</h1>
            <Navigation/>
            <Logo/>
            <Rank />
            <ImageLinkForm/>
{/*

            <FaceRecognition/>*/}
        </div>
    );
    }
}
export default App;
