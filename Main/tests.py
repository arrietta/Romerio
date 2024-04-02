from django.test import TestCase
from .models import Collections, Portal, Cart, CartItem, Doors


class ModelsTestCase(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.collection = Collections.objects.create(name="Test Collection", type="Test Type")
        self.portal = Portal.objects.create(name="Test Portal", price=100.0)
        self.cart = Cart.objects.create()

    def test_collections_model(self):
        # Проверяем, что модель Collections создана правильно
        collection = Collections.objects.get(name="Test Collection")
        self.assertEqual(collection.type, "Test Type")

    def test_portal_model(self):
        # Проверяем, что модель Portal создана правильно
        portal = Portal.objects.get(name="Test Portal")
        self.assertEqual(portal.price, 100.0)

    def test_cart_model(self):
        # Проверяем, что модель Cart создана правильно
        cart = Cart.objects.get(id=self.cart.id)
        self.assertIsNotNone(cart.user_token)

    def test_cartitem_model(self):
        # Создаем CartItem и связываем с базовой дверью
        cart_item = CartItem.objects.create(cart=self.cart, base_door=self.portal, quantity=2)

        # Проверяем, что CartItem создан успешно
        self.assertIsNotNone(cart_item)

        # Проверяем, что поле cart связано с корректным Cart
        self.assertEqual(cart_item.cart, self.cart)

        # Проверяем, что базовая дверь связана с корректным Portal
        self.assertEqual(cart_item.base_door, self.portal)

        # Проверяем, что количество товаров равно 2
        self.assertEqual(cart_item.quantity, 2)

        # Проверяем, что поля для других типов дверей равны None
        self.assertIsNone(cart_item.classic_door)
        self.assertIsNone(cart_item.classic_baguette)
        self.assertIsNone(cart_item.griglia_door)

    def test_door_price_calculation(self):
        # Создаем объект Doors
        door = Doors.objects.create(collection=self.collection, door_type="Test Door",
                                    door_image="test.jpg", shape="Square", shape_price=50.0,
                                    portal=self.portal, carnice=self.carnice, podium=self.podium,
                                    socket=self.socket, boots=self.boots)

        # Проверяем, что цена двери рассчитывается правильно
        expected_price = self.portal.price + self.carnice.price + self.podium.price + \
                         self.socket.price + self.boots.price + 50.0
        self.assertEqual(door.door_price, expected_price)
