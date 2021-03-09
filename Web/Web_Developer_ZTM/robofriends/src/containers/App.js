import React, { Component } from 'react'
import CardList from "../components/CardList";
import SearchBox from '../components/SearchBox'
import './App.css'
import Scroll from '../components/Scroll'

class App extends Component {
    constructor() {
        super();
        this.state = {
            robots: [],
            searchfield: ''
        }
    }
    componentDidMount() {
        fetch('https://jsonplaceholder.typicode.com/users')/* takes sample user data from an API*/
            .then(response =>  response.json()) /*convert the response to json*/
            .then(users => this.setState({robots: users})); /*set the state of the app to the recieved user data*/
        }

    onSearchChange = (event) => { /*function to change the data of our search field*/
        this.setState({ searchfield: event.target.value })
    }

    render() { /*this function will take the user input and use it to filter through the object with robots*/
        const filteredRobots = this.state.robots.filter(robot => {
            return robot.name.toLowerCase().includes(this.state.searchfield.toLowerCase());
        });
        if (!filteredRobots.length){
            return <h1>Loading...</h1>
        }
        return(
        <div className='tc'>
            <h1 style={{fontSize: '50px'}}>RoboFriends</h1>
            <h1 style={{fontSize: '25px'}}>Search for your Robo Friend!</h1>
            <SearchBox searchChange={this.onSearchChange}/>
            <Scroll>
                <CardList robots={filteredRobots}/> {/*load the filtered robot list, this will be the full list when search bar is empty*/}
            </Scroll>
        </div>
        );
    }
}
export default App