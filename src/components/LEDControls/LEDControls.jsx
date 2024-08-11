import React from 'react'
import ControlGroup from './ControlGroup/ControlGroup'

const LEDControls = () => {
    return (
        <div className='control-container'>
            <h1>LED Controls</h1>
            <ControlGroup color="red" />
            <ControlGroup color="yellow" />
            <ControlGroup color="green" />
            <ControlGroup color="blue" />
        </div>
    )
}

export default LEDControls