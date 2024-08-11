import React, { useState } from 'react'

const ControlGroup = ({ color }) => {

    const [message, setMessage] = useState("")
    const [errMessage, setErrMessage] = useState("")

    const ledOn = async (color) => {
        try {
            const data = await (await fetch(`/api/${color}-on`)).json()
            setMessage(data.message)
        } catch (err) {
            setErrMessage(err.message)
        }
    }
    const ledOff = async (color) => {
        try {
            const data = await (await fetch(`/api/${color}-off`)).json()
            setMessage(data.message)
        } catch (err) {
            setErrMessage(err.message)
        }
    }

    return (
        <div className='control-group'>
            <h2>{color} LED</h2>
            <p>Status: {message}</p>
            {errMessage && <p>errMessage</p>}
            <button onClick={() => ledOn(color)}>On</button>
            <button onClick={() => ledOff(color)}>Off</button>
        </div>
    )
}

export default ControlGroup