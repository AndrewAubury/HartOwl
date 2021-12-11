"""Sensor platform for integration_blueprint."""
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import IntegrationBlueprintEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([IntegrationBlueprintSensor(coordinator, entry)])


class IntegrationBlueprintSensor(IntegrationBlueprintEntity):
    """integration_blueprint Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
    @property
    def device_class(self):
        return "energy"
    @property
    def native_unit_of_measurement(self):
        return "Wh"