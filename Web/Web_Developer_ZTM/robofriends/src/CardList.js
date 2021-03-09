import React from 'react'
import Card from "./Card";
import {robots} from "./robots";

const CardList = ({robots}) =>{
    const cardComponents = robots.map((user, index) =>{ /*functions that maps returning a card to our list of of objects*/
        return <Card
            key={index}
            id={robots[index].name}
            name={robots[index].name}
            email={robots[index].email}/>
    })
    return(
        <div>
            {cardComponents} {/*call the function, returns all the cards from robots.js*/}
        </div>
    )
}
export default CardList;