import React from 'react';

const ImageLinkForm = ({onInputChange, onSubmit}) =>{ /*a logout button*/
    return(
        <div>
            <p
        className='f3 center tc'>
                {'This magic brain will detect your face!'}</p>
            <div className='pa5 br3 shadow-5'>
                <div>
                <input className='f4 pa2 w-70 center' type='text' onChange={onInputChange}/>
                <button style= {{alignContent: 'center'}}
                        className='w-30 grow f4 link ph3 pv2 dib white bg-light-purple center'
                    onClick = {onSubmit}
                    >Detect</button>
            </div>
            </div>
        </div>
    );
}

export default ImageLinkForm;