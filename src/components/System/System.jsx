import React, { useState, useEffect } from 'react';

const System = () => {

    const [sysInfo, setSysInfo] = useState({});

    useEffect(() => {
        fetch('/systeminfo').then(res => res.json()).then(data => {

            setSysInfo({
                time: Date(data.systime * 1000),
                machine: data.machine,
                platform: data.platform,
                system: data.system,
                version: data.version
            });

        });
    }, []);

    return (
        <div>
            <h1>System Information</h1>
            <p>Machine: <b>{sysInfo.machine}</b>.</p>
            <p>System: <b>{sysInfo.system}</b>.</p>
            <p>Platform: <b>{sysInfo.platform}</b>.</p>
            <p>Version: <b>{sysInfo.version}</b>.</p>
            <p>System time: <b>{sysInfo.time}</b>.</p>
        </div>
    )
}

export default System