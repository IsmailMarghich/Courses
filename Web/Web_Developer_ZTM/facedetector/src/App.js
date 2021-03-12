import './App.css';
import React, { Component} from 'react';
import Navigation from "./components/Navigation/Navigation";
import Logo from "./components/Logo/Logo";
import ImageLinkForm from "./components/ImageLinkForm/ImageLinkForm";
import Rank from "./components/Rank/Rank";
import Particles from "react-particles-js";
import Clarifai from 'clarifai'
import FaceRecognition from './components/FaceRecognition/FaceRecognition'
const app = new Clarifai.App({
    apiKey: 'b02f8720fe20454190112fa90dba9255'
});
const particleOptions = {
    "particles": {
        "number": {
            "value": 50
        },
        "size": {
            "value": 3
        }
    },
    "interactivity": {
        "events": {
            "onhover": {
                "enable": true,
                    "mode": "repulse"
            }
        }
    }
}

class App extends Component {
    constructor() {
        super();
        this.state = {
            input: '',
            imageUrl: '',
            box: {},
            route: 'signin',
            isSignedIn: false,
            user: {
                id: '',
                name: '',
                email: '',
                entries: 0,
                joined: ''
            }
        }
    }

    loadUser = (data) => {
        this.setState({user: {
                id: data.id,
                name: data.name,
                email: data.email,
                entries: data.entries,
                joined: data.joined
            }})
    }
    onInputChange = (event) =>{
    console.log(event.target.value);
    }
    onSubmit = () => {
        this.setState({imageUrl: this.state.input});
        app.models
            .predict(
                // HEADS UP! Sometimes the Clarifai Models can be down or not working as they are constantly getting updated.
                // A good way to check if the model you are using is up, is to check them on the clarifai website. For example,
                // for the Face Detect Mode: https://www.clarifai.com/models/face-detection
                // If that isn't working, then that means you will have to wait until their servers are back up. Another solution
                // is to use a different version of their model that works like: `c0c0ac362b03416da06ab3fa36fb58e3`
                // so you would change from:
                // .predict(Clarifai.FACE_DETECT_MODEL, this.state.input)
                // to:
                // .predict('c0c0ac362b03416da06ab3fa36fb58e3', this.state.input)
                'c0c0ac362b03416da06ab3fa36fb58e3', this.state.input)
            .then(response => {
                console.log('hi', response)
                if (response) {
                    fetch('https://pbs.twimg.com/profile_images/1116799956013203462/WOX874ki.png', {
                        method: 'put',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            id: this.state.user.id
                        })
                    })
                        .then(response => response.json())
                        .then(count => {
                            console.log(response);
                            this.setState(Object.assign(this.state.user, { entries: count}))
                        })

                }
            })
            .catch(err => console.log(err));
    }

    render() {
        return (
        <div className="App">
            <Particles className='particles'
                params={particleOptions} />
            <h1>Face Detector</h1>
            <Navigation/>
            <Logo/>
            <Rank />
            <ImageLinkForm onInputChange={this.onInputChange}
                           onSubmit = {this.onSubmit}/>
            <FaceRecognition onSubmit = {this.imageUrl}
            />
        </div>
    );
    }
}
export default App;
