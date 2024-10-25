import styles from "./search_bar.module.css";
import Zlatmax_logo from "../assets/Zlatmax_logo.png";
import Location_logo from "../assets/Location_logo.png";
import Favorites_logo from "../assets/Favorites_logo.png";
import Cart_logo from "../assets/Cart_logo.png";
import VectorDown from "../../Assets/Vector-down.png";
export const SearchBar = () => {
  return (
    <div className={styles.search_bar_container}>
      <div>
        <img src={Zlatmax_logo} alt="logo" />
      </div>
      <div>
        <input className={styles.search_bar_input} type="text" placeholder="🔍︎ Поиск" />
      </div>
      <div className={styles.search_bar_right_side}>
        <div className={styles.search_bar_location}>
          <img src={Location_logo} alt="location logo" />
          <span>Москва</span>
        </div>
        <div className={styles.search_bar_phone}>
          <div>
            8-800-777-49-67 <img className={styles.vector_down} src={VectorDown} alt="VectorDown" />
          </div>
          <span>Заказать звонок</span>
        </div>
        <div>
          <img src={Favorites_logo} alt="Favorites_logo" />
        </div>
        <div className={styles.search_bar_cart_block}>
          <div className={styles.search_bar_cart}>
            <img src={Cart_logo} alt="Cart_logo" />
            <div className={styles.search_bar_cart_number}>5</div>
          </div>
          <div className={styles.search_bar_cart_price}>
            <p >0 р.</p>
            <div>Оформить заказ</div>
          </div>
        </div>
      </div>
    </div>
  );
};
