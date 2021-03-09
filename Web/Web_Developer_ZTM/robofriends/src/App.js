import React, { Component } from 'react'
import CardList from "./CardList";
import {robots} from "./robots";
import SearchBox from './SearchBox'



class App extends Component {
    constructor() {
        super();
        this.state = {
            robots: robots,
            searchfield: ''
        }
    }
    onSearchChange = (event) => { /*function to change the data of our search field*/
        this.setState({ searchfield: event.target.value })
    }

    render() { /*this function will take the user input and use it to filter through the object with robots*/
        const filteredRobots = robots.filter(robot => {
            return robot.name.toLowerCase().includes(this.state.searchfield.toLowerCase());
        });
        return(
        <div className='tc'>
            <h1>RoboFriends</h1>
            <SearchBox searchChange={this.onSearchChange}/>
            <CardList robots={filteredRobots}/>
        </div>
        );
    }
}
export default App