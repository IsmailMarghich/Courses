import React from 'react'
/*we want the search bar to be accesible when the user scrolls down, so we can add a scroll bar to our card list*/
const Scroll = (props) =>{
    return (
        <div style={{overflowY: 'scroll', border: '5px solid back', height: '700px'}}> {/*css style to make element scrollable*/}
            {props.children};
        </div>
    )
};
export default Scroll