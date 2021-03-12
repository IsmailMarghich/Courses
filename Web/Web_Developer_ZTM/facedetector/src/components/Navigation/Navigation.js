import React from 'react';


const Navigation = () =>{ /*a logout button*/
    return(
        <nav style = {{display: 'flex', justifyContent: 'flex-end'}}>  {/*locate it top right*/}
            <p className='f3 link dim black pa3 pointer red'> Sign Out</p> {/*styles to make it look like a logout button*/}
        </nav>
    );
}

export default Navigation;