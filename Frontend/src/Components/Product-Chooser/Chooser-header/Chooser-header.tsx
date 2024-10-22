import styles from "./chooser-header.module.css";
export const ChooserHeader = () => {
    return (
        <div className={styles.chooser_header_container}>
            <ul className={styles.chooser_header_list}>
                <li>Каталог ножей</li>
                <li>Клинковое оружие</li>
                <li>Сувенирные изделия</li>
                <li>Фонари ARMYTEK</li>
                <li>Сопуствующие товары</li>
            </ul>
        </div>
    );
}