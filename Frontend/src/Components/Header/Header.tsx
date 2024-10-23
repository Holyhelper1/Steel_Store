import styles from "./header.module.css";
import Account_logo from "./assets/Account_logo.png";

export const Header = () => {
  return (
    <div className={styles.header_container}>
      <div >
        <ul className={styles.header_left_side}>
          <li>О нас</li>
          <li>Оплата и доставка</li>
          <li>Новости</li>
          <li>Контакты</li>
        </ul>
      </div>

      <div>
        <ul className={styles.header_right_side}>
          <li>
            <img src={Account_logo} alt="Account logo" />
          </li>
          <li>Личный кабинет</li>
        </ul>
      </div>
    </div>
  );
};
