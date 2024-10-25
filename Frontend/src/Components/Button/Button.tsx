import styles from "./main-button.module.css"
export const Button = ({children}: {children: React.ReactNode}) => {
    return (
        <div  className={styles.button_box}>
            <button className={styles.button_container}>{children}</button>
        </div>
    );
}