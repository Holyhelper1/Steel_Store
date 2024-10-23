import styles from "./footer-top.module.css";
export const FooterTop = () => {
  return (
      <div className={styles.footer_top_container}>
        <div className={styles.footer_ul_container}>
          <ul>
            <li>
              <span> ИНФОРМАЦИЯ </span>
            </li>
            <li>Златоустовские ножи в Москве и Московской области</li>
            <li>Ножевые стали</li>
            <li>О нас</li>
            <li>Условия оплаты и доставки</li>
            <li>Политика конфиденциальности</li>
          </ul>
        </div>
        <div className={styles.footer_ul_container}>
          <ul>
            <li><span>  СЛУЖБА ПОДДЕРЖКИ</span></li>
            <li>Контактная информация</li>
            <li>Возврат товара</li>
            <li>Карта сайта</li>
          </ul>
        </div>
        <div className={styles.footer_ul_container}>
          <ul>
            <li><span>ДОПОЛНИТЕЛЬНО</span></li>
            <li>Подарочные сертификаты</li>
            <li>Партнеры</li>
            <li>Товары со скидкой</li>
          </ul>
        </div>
        <div className={styles.footer_ul_container}>
          <ul>
            <li><span>ЛИЧНЫЙ КАБИНЕТ</span></li>
            <li>Личный кабинет</li>
            <li>История заказов</li>
            <li>Мои закладки</li>
            <li>Рассылка новостей</li>
          </ul>
        </div>
        
      </div>
    
  );
};
