import React from 'react';

const Card = ({name, email, id }) =>{ /*this prop takes the information from robots.js to make a card*/
    return(
        <div className={'bg-light-green dib br3 ma2 grow tc bw2 shadow-5'}> {/*css styling*/}
            <img src={`https://robohash.org/${id}?size=200x200`} /> {/*grab an image from the API, based on the id*/}
            <div>
                <h2>{name}</h2> {/*display name*/}
                <p>{email.toLowerCase()}</p> {/*display email, convert to lower case*/}
            </div>
        </div>
    )
}
export default Card;