import React from 'react';
import Tilt from 'react-tilt'
import './logo.css'
import Brain from './icon.png'
const Logo = () =>{ /*a cool logo*/
    return(
        <div className='margin 3  pa3 mt0 '> {/*styling for logo*/}
            <Tilt className="Tilt br2 shadow-2" options={{ max : 45 }} style={{ height: 92, width: 92 }} > {/*tilting animation when u hover the logo*/}
                <div className="Tilt-inner" pa3>
                    <img style={{paddingTop: '5px'}}
                         src={Brain}/> </div>{/*add padding and make image fit the container*/}
            </Tilt>
        </div>
    );
};

export default Logo;