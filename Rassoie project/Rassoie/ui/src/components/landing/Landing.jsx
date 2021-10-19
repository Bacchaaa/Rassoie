import React from 'react';
import style from './Landing.module.css'

function Landing() {
    return (
        <section className={style.landing}>
            <div className={style.overlay}>
                <h1 className={style.mainheading}>Rassoie</h1>
                <h3>EAT GOOD, FEEL GOOD</h3>
            </div>
        </section>
    )
}

export default Landing
